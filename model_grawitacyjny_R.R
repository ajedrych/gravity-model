# EKIiE Z06

# Zadanie 1
library("readxl")
df = read_excel("gravity2.xlsx")
View(df)

options(scipen=999)

# model - wersja 1
model1 = lm(ln_import~ln_distance + common_language + colonial_dependency +population_i + population_j +ln_gdp_i + ln_gdp_j+ gdp_per_capita_i + gdp_per_capita_j+
              gatt_i + gatt_j + wto_i + wto_j +eu_i + eu_j + rta +entry_cost_i + entry_cost_j + entry_procedures_i + entry_procedures_j +
              entry_time_i + entry_time_j + AD_initations_i + AD_initations_j + AD_measures_i + AD_measures_j, data=df)
summary(model1)

#usuwamy colonial_dependency, poniewaz jest nieistotna statystycznie
#model2
model2 = lm(ln_import~ln_distance + common_language + population_i + population_j +ln_gdp_i + ln_gdp_j+ gdp_per_capita_i + gdp_per_capita_j+
              gatt_i + gatt_j + wto_i + wto_j +eu_i + eu_j + rta +entry_cost_i + entry_cost_j + entry_procedures_i + entry_procedures_j +
              entry_time_i + entry_time_j + AD_initations_i + AD_initations_j + AD_measures_i + AD_measures_j, data=df)
summary(model2)

#model3 usuwamy ad_initations_i
model3 = lm(ln_import~ln_distance + common_language + population_i + population_j +ln_gdp_i + ln_gdp_j+ gdp_per_capita_i + gdp_per_capita_j+
              gatt_i + gatt_j + wto_i + wto_j +eu_i + eu_j + rta +entry_cost_i + entry_cost_j + entry_procedures_i + entry_procedures_j +
              entry_time_i + entry_time_j + AD_initations_j + AD_measures_i + AD_measures_j, data=df)
summary(model3)

#model 4 usuwamy entry time i
model4 = lm(ln_import~ln_distance + common_language + population_i + population_j +ln_gdp_i + ln_gdp_j+ gdp_per_capita_i + gdp_per_capita_j+
              gatt_i + gatt_j + wto_i + wto_j +eu_i + eu_j + rta +entry_cost_i + entry_cost_j + entry_procedures_i + entry_procedures_j +
              entry_time_j + AD_initations_j + AD_measures_i + AD_measures_j, data=df)
summary(model4)



# tablica w stylu publikacyjnym
# Quality Publication Table
library("stargazer")
stargazer(model1,model2, model3, model4, type= "text", title = "Estymowane modele: podsumowanie", out="model1.txt")
stargazer(model1, model2, model3, model4, type="html", 
          align=TRUE, style="default", df=FALSE)
stargazer(model1, model2, model3, model4, type="text", 
          align=TRUE, style="default", df=FALSE)

stargazer(model1,  type="text", 
          align=TRUE, style="default", df=TRUE)

stargazer(model1, type="text", 
          align=TRUE, style="default", df=FALSE, star.cutoffs =c(0.05, 0.01, 0.001))

#test reset
library("lmtest")
library("foreign")
resettest(model4, power=2:3, type="fitted")
#p-value < 0.05 czyli odrzucamy h0 o prawidłowej formie funkcyjnej

resettest(model5, power=2:3, type="regressor")
