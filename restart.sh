set -x

MY_INSTANCE_NAME="manhamprod"
ZONE=europe-west1-b

gcloud compute instances stop $MY_INSTANCE_NAME --zone $ZONE

gcloud compute instances start $MY_INSTANCE_NAME --zone $ZONE

gcloud compute instances get-serial-port-output $MY_INSTANCE_NAME --zone $ZONE

gcloud compute instances list