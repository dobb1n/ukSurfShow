resource "google_cloud_scheduler_job" "trigger_pod_grabber" {
  name             = "trigger-pod-grabber"
  description      = "Triggers the Cloud Run pod grabber function"
  schedule         = "0 3 * * *"
  time_zone        = "Europe/London"

  http_target {
    http_method = "GET"
    uri         = "https://pod-grabber-335831825547.europe-west2.run.app"

    # Optional headers
    headers = {
      "Content-Type" = "application/json"
      "User-Agent"   = "terraform-scheduler"
    }
  }
}