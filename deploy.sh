set -ex

MY_INSTANCE_NAME="manhamprod"
ZONE=europe-west1-b

gcloud compute instances create $MY_INSTANCE_NAME \
    --image-family=debian-10 \
    --image-project=debian-cloud \
    --machine-type=c2-standard-8 \
    --scopes userinfo-email,cloud-platform \
    --metadata-from-file startup-script=startup_script.sh \
    --zone $ZONE \
    --tags https-server
# [END getting_started_gce_create_instance]

gcloud compute firewall-rules create default-allow-https-8080 \
    --allow tcp:8080 \
    --source-ranges 0.0.0.0/0 \
    --target-tags https-server \
    --description "Allow port 8080 access to https-server"
