# RetinaLiteClassifier

This classifier is a model based off the paper RetinaLiteNet. We recreated their encoder and MHA bottleneck and added a classifier head on the end to see how their structure does on a classification setting.

## Testing
### RetinaLiteNet
We first recreated their model and trained it

### RetinaLiteClassifier
Using their retrained model we tested our classifier using our pretrained weights for the encoder and bottleneck then trained once without it and compared.
