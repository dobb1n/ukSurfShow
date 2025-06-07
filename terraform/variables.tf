variable "project_id" {
  description = "The ID of the GCP project to deploy resources to"
  type        = string
}

variable "region" {
  description = "The GCP region to deploy resources in"
  type        = string
  default     = "europe-west2"
}