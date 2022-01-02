# EKIiE Z06

# Zadanie 1
library("readxl")
df = read_excel("gravity2.xlsx")
View(df)

options(scipen=999)

# model - wersja 1
model1 = lm(ln_import~ln_distance + common_language + colonial_dependency +population_i + population_j +ln_gdp_i + ln_gdp_j+ gdp_per_capita_i + gdp_per_capita_j+
              gatt_i + gatt_j + wto_i + wto_j +eu_i + eu_j + rta +entry_cost_i + entry_cost_j + entry_procedures_i + entry_procedures_j +
              entry_time_i + entry_time_j +entry_tp_i +entry_tp_j + AD_initations_i + AD_initations_j + AD_measures_i + AD_measures_j, data=df)
summary(model1)

na.omit(df)

#usuwamy entry_tp_i i entry_tp_j

#model2
model2 = lm(ln_import~ln_distance + common_language + colonial_dependency +population_i + population_j +ln_gdp_i + ln_gdp_j+ gdp_per_capita_i + gdp_per_capita_j+
              gatt_i + gatt_j + wto_i + wto_j +eu_i + eu_j + rta +entry_cost_i + entry_cost_j + entry_procedures_i + entry_procedures_j +
              entry_time_i + entry_time_j + AD_initations_i + AD_initations_j + AD_measures_i + AD_measures_j, data=df)
summary(model2)

#model 3
model3 = lm(ln_import~ln_distance + common_language + population_i + population_j +ln_gdp_i + ln_gdp_j+ gdp_per_capita_i + gdp_per_capita_j+
              gatt_i + gatt_j + wto_i + wto_j +eu_i + eu_j + rta +entry_cost_i + entry_cost_j + entry_procedures_i + entry_procedures_j +
              entry_time_i + entry_time_j + AD_initations_i + AD_initations_j + AD_measures_i + AD_measures_j, data=df)
summary(model3)

#model 4 wywalam ad_initations_i
model4 = lm(ln_import~ln_distance + common_language + population_i + population_j +ln_gdp_i + ln_gdp_j+ gdp_per_capita_i + gdp_per_capita_j+
              gatt_i + gatt_j + wto_i + wto_j +eu_i + eu_j + rta +entry_cost_i + entry_cost_j + entry_procedures_i + entry_procedures_j +
              entry_time_i + entry_time_j + AD_initations_j + AD_measures_i + AD_measures_j, data=df)
summary(model4)

#model5 wywalam entry_time_i
model5 = lm(ln_import~ln_distance + common_language + population_i + population_j +ln_gdp_i + ln_gdp_j+ gdp_per_capita_i + gdp_per_capita_j+
              gatt_i + gatt_j + wto_i + wto_j +eu_i + eu_j + rta +entry_cost_i + entry_cost_j + entry_procedures_i + entry_procedures_j +
              entry_time_j + AD_initations_j + AD_measures_i + AD_measures_j, data=df)
summary(model5)


# tablica w stylu publikacyjnym
# Quality Publication Table
library("stargazer")
stargazer(model1, model2, model3, model4, model5, type="text", 
          align=TRUE, style="default", df=FALSE)

stargazer(model1, model2, model3, model4, model5, type="text", 
          align=TRUE, style="default", df=TRUE)

stargazer(model1, model2, model3, model4, model5, type="text", 
          align=TRUE, style="default", df=FALSE, star.cutoffs =c(0.05, 0.01, 0.001))


library("car")
linearHypothesis(model=model1, c("klm2=0", "klm3=0", "klm4=0", "klm5=0", "klm6=0"))

# w konwencji H*Beta=h
h = rep(0, times=5)
H = cbind(matrix(0, ncol=3, nrow=5), diag(5), matrix(0, ncol=2, nrow=5))
linearHypothesis(model=model1, rhs=h, hypothesis.matrix=H)

# istotnosc zmiennej klm2 w modelu (1)
options(scipen=5)
# options(scipen=999)
summary(model1)$coefficients

tab_oszacowan = summary(model1)$coefficients
tab_oszacowan[1,1]
# reczne testowanie istotnosci zmiennej klm2
(t_test = (tab_oszacowan[4,1]-0)/tab_oszacowan[4,2])
df = model1$df
df
# p-value
(p_value = 2*(1-pt(q=abs(t_test), df=df)))

# testowanie hipotezy H0: beta_klm5 = -5
(t_test = (tab_oszacowan[7,1]-(-5))/tab_oszacowan[7,2])
df = model1$df
# p-value
(p_value = 2*(1-pt(q=abs(t_test), df=df)))


# Zadanie 7
diamonds = read.dta(file="diamonds.dta")
View(diamonds)

model = lm(price~as.numeric(carat)+as.factor(colour)+as.factor(clarity), 
           data=diamonds)
summary(model)
plot(model)
plot(model, which=5)



