library(azuremlsdk)

packageVersion('azuremlsdk')

tenant_id <- Sys.getenv("TENANT_ID")
svc_pr_secret <- Sys.getenv("SERVICE_PRINCIPAL_SECRET")
svc_pr_id <- Sys.getenv("SERVICE_PRINCIPAL_ID")

ws_name <- Sys.getenv("WORKSPACE_NAME")
rg <- Sys.getenv("RESOURCE_GROUP")
sub_id <- Sys.getenv("SUBSCRIPTION_ID")

sp_auth <- service_principal_authentication(
    tenant_id,
    svc_pr_id,
    svc_pr_secret,
    cloud = "AzureCloud"
)

ws <- get_workspace(ws_name, auth=sp_auth, subscription_id = sub_id, resource_group=rg)

ds <- get_default_datastore(ws)

print(ws)

print(ds)