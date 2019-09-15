install.packages(c("rmarkdown", "dplyr","knitr", "kableExtra"))
library(rmarkdown)
render("./report/report.Rmd", "all")