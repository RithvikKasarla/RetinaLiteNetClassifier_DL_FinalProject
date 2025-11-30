# RetinaLiteClassifier

This classifier is a model based on the paper RetinaLiteNet. We recreated their encoder and MHA bottleneck and added a classifier head on the end to see how their structure does in a classification setting.

## Testing
### RetinaLiteNet
We first recreated their model and trained it

### RetinaLiteClassifier
Using their retrained model, we tested our classifier using our pretrained weights for the encoder and bottleneck, then trained once without it and compared.

#### Pivots 
In the RetinaLiteClassifier.ipynb, we have it tested against other subproblems and classifiers again to see how they compare. We later reformatted the problem as Healthy vs Not Healthy and understood how the model did in that case, too.
