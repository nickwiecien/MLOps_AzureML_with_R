library(azuremlsdk)

ws <- get_workspace('parker_aml_ws')

ds <- get_default_datastore(ws)

print(ws)