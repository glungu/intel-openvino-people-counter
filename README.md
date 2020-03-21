# intel-openvino-people-counter

## Model Selection 
Models were selected from the [Tensorflow Object Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md). The following two model were tried:

* ssd_inception_v2_coco
* faster_rcnn_inception_v2_coco

The SSD model had good latency (~150 microseconds per frame), but lacked accuracy and failed to detect some people in the video.
Faster-RCNN had bigger latency (~950 microseconds per frame), but provided good accuracy for this project. Stably detecting a person in the frame when he/she was there and vise versa is important for counting duration, and detecting person enter/exit.

## Model Optimization
The following three laters were unsupported by the core Model Optimizer:
* Layer proposals is not supported
* Layer Squeeze_3 is not supported
* Layer detection_output is not supported

But with the use of OpenVINO's faster_rcnn_support extension, all layers were supported, and the TF Model was successfully converted in IR format by the Model Optimizer. The following command was used:

```sh
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model faster_rcnn_inception_v2_coco_2018_01_28/frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config faster_rcnn_inception_v2_coco_2018_01_28/pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/faster_rcnn_support.json
```

## Running without OpenVINO™ Toolkit
Run the pre-trained model without the use of the OpenVINO™ Toolkit. Compare the performance of the model with and without the use of the toolkit (size, speed, CPU overhead). What about differences in network needs and costs of using cloud services as opposed to at the edge?

