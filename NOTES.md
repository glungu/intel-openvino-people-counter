# Project Notes

## Initialize Python Virtual Env
```commandline
source /opt/intel/openvino/bin/setupvars.sh -pyver 3.5
```

## MQTT / Mosca
```commandline
cd webservice/server/node-server
node ./server.js
```

## FFServer
```commandline
sudo ffserver -f ./ffmpeg/server.conf
```


## UI Server
```commandline
cd webservice/ui
npm run dev
```

## Application
Converting the video for debugging purposes:
```commandline
python main_converter_openvino.py -i resources/Pedestrian_Detect_2_1_1.mp4 -pt 0.2 -m model/faster_rcnn_inception_v2_coco.xml 
```

Run application to send stats to MQTT and frames to stdout (for ffserver): 
```commandline
python main.py -i resources/Pedestrian_Detect_2_1_1.mp4 -m model/faster_rcnn_inception_v2_coco.xml -l /opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so -d CPU -pt 0.2 | ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm
```

## OpenVINO Model Optimizer options
 
* `--input_model` - Tensorflow .pb file 
* `--output_dir` - Output dir for OpenVINO IR files
* `--tensorflow_object_detection_api_pipeline_config` - Tensorflow pipeline.config file 
* `--reverse_input_channels` (BGR to RGB)
* `--tensorflow_use_custom_operations_config` - OpenVINO Tensorflow extension

Example command for SSD model:     
```commandline
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_v2_support.json
```
Example command for Faster-RCNN models: 
```commandline
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model faster_rcnn_inception_v2_coco_2018_01_28/frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config faster_rcnn_inception_v2_coco_2018_01_28/pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/faster_rcnn_support.json
```

## OpenVINO Extension Library to use during inference
```
/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so (or avx)
```

## Intel OpenVINO Issue on Windows 
This issue with cmake prevented using the local environment: 
[#850570 CMake error when running verification script](https://software.intel.com/en-us/forums/intel-distribution-of-openvino-toolkit/topic/850570)



