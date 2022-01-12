library(azuremlsdk)

packageVersion('azuremlsdk')

test_var <- Sys.getenv("HELLO")
print(test_var)

ws <- load_workspace_from_config()

ds <- get_default_datastore(ws)

print(ws)