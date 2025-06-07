resource "google_project_service" "cloud_scheduler" {
  service = "cloudscheduler.googleapis.com"
  project = var.project_id

  disable_on_destroy = false
}