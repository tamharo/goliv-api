MY_INSTANCE_NAME="manhamprod"
ZONE=europe-west1-b

gcloud compute instances create $MY_INSTANCE_NAME \
    --image-family=debian-10 \
    --image-project=debian-cloud \
    --project=goliv-c7734 
    --machine-type=e2-medium \
    --scopes userinfo-email,cloud-platform \
    --metadata-from-file startup-script=startup.sh \
    --zone $ZONE \
    --tags http-server