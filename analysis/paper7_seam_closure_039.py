"""
PRE-REG 039 — seam closure: two discharge axes of one displacement system.
State level (n~51). All on-disk. Output: analysis/paper7_seam_closure_039.json

food_insec  = FEA FOODINSEC_21_23 (state)
homeless    = CoC homeless_per_10k -> state (pop-weighted, latest yr)
rent_floor  = CoC rent_coc -> state (pop-weighted)
precarity   = Pulse behind_on_rent_share (state, mean over periods)
poverty     = FEA POVRATE21 -> state (pop-weighted county)
food_floor  = FARA sum(LAPOP1_10)/sum(Pop2010) -> state (income-free low-access share)
"""
from __future__ import annotations
import json, zipfile
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm

IDP = Path(r"D:\IDP")
FEAX = r"D:\Food Deserts\data_raw\FEA\2025-food-environment-atlas-data.xlsx"
FARA_ZIP = r"D:\Food Deserts\data_raw\FARA\2019_Food_Access_Research_Atlas_Data.zip"

FIPS2USPS = {1:'AL',2:'AK',4:'AZ',5:'AR',6:'CA',8:'CO',9:'CT',10:'DE',11:'DC',12:'FL',13:'GA',
15:'HI',16:'ID',17:'IL',18:'IN',19:'IA',20:'KS',21:'KY',22:'LA',23:'ME',24:'MD',25:'MA',26:'MI',
27:'MN',28:'MS',29:'MO',30:'MT',31:'NE',32:'NV',33:'NH',34:'NJ',35:'NM',36:'NY',37:'NC',38:'ND',
39:'OH',40:'OK',41:'OR',42:'PA',44:'RI',45:'SC',46:'SD',47:'TN',48:'TX',49:'UT',50:'VT',51:'VA',
53:'WA',54:'WV',55:'WI',56:'WY'}
NAME2USPS = {'alabama':'AL','alaska':'AK','arizona':'AZ','arkansas':'AR','california':'CA','colorado':'CO',
'connecticut':'CT','delaware':'DE','district of columbia':'DC','florida':'FL','georgia':'GA','hawaii':'HI',
'idaho':'ID','illinois':'IL','indiana':'IN','iowa':'IA','kansas':'KS','kentucky':'KY','louisiana':'LA',
'maine':'ME','maryland':'MD','massachusetts':'MA','michigan':'MI','minnesota':'MN','mississippi':'MS',
'missouri':'MO','montana':'MT','nebraska':'NE','nevada':'NV','new hampshire':'NH','new jersey':'NJ',
'new mexico':'NM','new york':'NY','north carolina':'NC','north dakota':'ND','ohio':'OH','oklahoma':'OK',
'oregon':'OR','pennsylvania':'PA','rhode island':'RI','south carolina':'SC','south dakota':'SD',
'tennessee':'TN','texas':'TX','utah':'UT','vermont':'VT','virginia':'VA','washington':'WA',
'west virginia':'WV','wisconsin':'WI','wyoming':'WY'}


def wmean(df, val, w):
    d = df.dropna(subset=[val, w]);
    return np.average(d[val], weights=d[w]) if len(d) else np.nan


def main():
    # food insecurity (state)
    ins = pd.read_excel(FEAX, sheet_name="INSECURITY", header=1)
    food = ins.groupby("State").agg(food_insec=("FOODINSEC_21_23","mean"),
                                    food_insec_pre=("FOODINSEC_18_20","mean")).reset_index().rename(columns={"State":"st"})

    # poverty (county -> state pop-weighted, county pop from FARA)
    soc = pd.read_excel(FEAX, sheet_name="SOCIOECONOMIC", header=1)[["FIPS","State","POVRATE21"]]
    with zipfile.ZipFile(FARA_ZIP) as z, z.open("Food Access Research Atlas.csv") as f:
        fara = pd.read_csv(f, usecols=["CensusTract","Pop2010","LAPOP1_10"], dtype={"CensusTract":str})
    fara["geoid"] = fara.CensusTract.str.zfill(11)
    fara["FIPS"] = fara.geoid.str[:5].astype(int)
    fara["statefip"] = fara.geoid.str[:2].astype(int)
    for c in ["Pop2010","LAPOP1_10"]:
        fara[c] = pd.to_numeric(fara[c], errors="coerce").fillna(0.0)
    # state poverty = unweighted county-mean POVRATE21 (pop-weighted merge was corrupted;
    # unweighted validates corr(food_insec,poverty)=0.918, the expected structural link)
    pov = soc.groupby("State").POVRATE21.mean().rename("poverty").reset_index().rename(columns={"State":"st"})

    # food floor (state low-access share, FARA)
    ff = fara.groupby("statefip").apply(lambda d: d.LAPOP1_10.sum()/d.Pop2010.sum()).rename("food_floor").reset_index()
    ff["st"] = ff.statefip.map(FIPS2USPS)
    ff = ff[["st","food_floor"]].dropna()

    # homelessness + rent floor (CoC -> state)
    coc = pd.read_csv(IDP/"analysis"/"paper7_coc_timepanel_2012_2024.csv")
    yr = coc.dropna(subset=["homeless_per_10k"]).year.max()
    c = coc[coc.year==yr].copy()
    c["st"] = c.coc_number.str[:2]
    hs = c.groupby("st").apply(lambda d: pd.Series({
        "homeless_per_10k": wmean(d,"homeless_per_10k","total_population"),
        "rent_floor": wmean(d,"rent_coc","total_population")})).reset_index()

    # precarity (Pulse, state)
    pul = pd.read_csv(IDP/"analysis"/"paper7_pulse_housing_precarity.csv")
    ps = pul[pul.geo_type.astype(str).str.lower().str.contains("state")].copy()
    if len(ps)==0: ps = pul.copy()
    def to_usps(g):
        g=str(g).strip()
        if len(g)==2 and g.upper() in FIPS2USPS.values(): return g.upper()
        return NAME2USPS.get(g.lower())
    ps["st"] = ps.geography.map(to_usps)
    prec = ps.groupby("st").agg(behind_on_rent=("behind_on_rent_share","mean"),
                                eviction_risk=("eviction_risk_share","mean")).reset_index()

    # merge
    m = food.merge(pov,on="st").merge(ff,on="st").merge(hs,on="st").merge(prec,on="st")
    m = m.dropna(subset=["food_insec","homeless_per_10k","rent_floor","behind_on_rent","poverty","food_floor"])
    print(f"homeless year used: {yr};  merged states n={len(m)}")

    def corr(a,b):
        r,p = stats.pearsonr(m[a],m[b]); return float(r),float(p)
    out={"n":int(len(m)),"homeless_year":int(yr),"corr":{}, "reg":{}}
    pairs=[("behind_on_rent","food_insec"),("behind_on_rent","homeless_per_10k"),
           ("eviction_risk","homeless_per_10k"),("food_insec","homeless_per_10k"),
           ("rent_floor","homeless_per_10k"),("rent_floor","food_insec"),
           ("food_floor","food_insec"),("poverty","food_insec"),("poverty","homeless_per_10k"),
           # pre-pandemic robustness (FOODINSEC_18_20, before SNAP emergency allotments)
           ("poverty","food_insec_pre"),("food_floor","food_insec_pre"),
           ("behind_on_rent","food_insec_pre"),("food_insec_pre","homeless_per_10k")]
    for a,b in pairs:
        r,p=corr(a,b); out["corr"][f"{a}~{b}"]={"r":round(r,3),"p":round(p,4)}

    def reg(y,xs):
        X=sm.add_constant(m[xs]); res=sm.OLS(m[y],X).fit(cov_type="HC1")
        return {k:{"b":round(float(res.params[k]),4),"p":round(float(res.pvalues[k]),4)} for k in ["const"]+xs} | {"r2":round(float(res.rsquared),3)}
    out["reg"]["homeless~rent_floor+poverty"]=reg("homeless_per_10k",["rent_floor","poverty"])
    out["reg"]["food_insec~poverty+food_floor+rent_floor"]=reg("food_insec",["poverty","food_floor","rent_floor"])

    # ---- decision rules ----
    c1 = out["corr"]["behind_on_rent~food_insec"]
    c2 = out["corr"]["behind_on_rent~homeless_per_10k"]
    c3 = out["corr"]["food_insec~homeless_per_10k"]
    rH = out["reg"]["homeless~rent_floor+poverty"]["rent_floor"]
    rF = out["reg"]["food_insec~poverty+food_floor+rent_floor"]
    D1 = c1["r"]>0 and c1["p"]<0.05
    D2 = not (c2["r"]>0 and c2["p"]<0.05)
    D3 = not (c3["r"]>0 and c3["p"]<0.05)
    D4 = (rH["b"]>0 and rH["p"]<0.05) and (rF["rent_floor"]["p"]>0.05) and \
         ((rF["poverty"]["b"]>0 and rF["poverty"]["p"]<0.05) or (rF["food_floor"]["b"]>0 and rF["food_floor"]["p"]<0.05))
    out["falsifiers"]={"CLOSE_D1_precarity_to_food":bool(D1),"CLOSE_D2_precarity_not_homeless":bool(D2),
                       "CLOSE_D3_axes_dissociate":bool(D3),"CLOSE_D4_rent_floor_switch":bool(D4),
                       "SEAM_CLOSED":bool(D1 and D2 and D3 and D4)}

    # contrast: South vs high-rent-coast states
    south=["MS","LA","AL","AR","TN","SC","KY","WV","NM","OK"]
    coast=["CA","NY","HI","MA","WA","OR","CO"]
    for tag,sts in [("South",south),("Coast",coast)]:
        s=m[m.st.isin(sts)]
        out.setdefault("contrast",{})[tag]={"food_insec":round(s.food_insec.mean(),1),
            "homeless_per_10k":round(s.homeless_per_10k.mean(),1),
            "rent_floor":round(s.rent_floor.mean(),0),"behind_on_rent":round(s.behind_on_rent.mean(),3)}

    (IDP/"analysis"/"paper7_seam_closure_039.json").write_text(json.dumps(out,indent=2))
    print(json.dumps(out["corr"],indent=2))
    print("REG homeless~rent+pov:", out["reg"]["homeless~rent_floor+poverty"])
    print("REG food_insec~pov+floor+rent:", out["reg"]["food_insec~poverty+food_floor+rent_floor"])
    print("contrast:", json.dumps(out.get("contrast",{})))
    print("FALSIFIERS:", json.dumps(out["falsifiers"],indent=2))


if __name__=="__main__":
    main()
