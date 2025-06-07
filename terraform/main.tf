terraform {
  backend "gcs" {
    bucket  = "transcribed-audio-files-b"
    prefix  = "tfstate"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}