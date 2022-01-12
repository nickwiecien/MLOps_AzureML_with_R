library(azuremlsdk)

ws <- load_workspace_from_config()

ds <- get_default_datastore(ws)

print(ws)