# import torch
# import openvino as ov

# # Load the PyTorch model
# model = torch.load("preTrained data\\yolov8n.pt")

# # Convert the PyTorch model to ONNX format
# dummy_input = torch.randn(1, 3, 416, 416)  # Provide a dummy input shape

# print(dummy_input)

# onnx_model_path = "model.onnx"
# torch.onnx.export(model, dummy_input, onnx_model_path)

# # Convert the ONNX model to OpenVINO IR format
# ov_model = ov.Model(onnx_model_path)
# ov_model.optimize()

# # Create an instance of the OpenVINO Core
# core = ov.Core()

# # Compile the model for GPU
# compiled_model = core.compile_model(ov_model, "GPU")

# # Perform inference using the compiled model
# input_data = ...  # Prepare your input data
# output_data = compiled_model.run(input_data)

# # Process the output data

"""from ultralytics import YOLO



model = YOLO("yolov8n.pt")  
# results = model.predict(source="https://ultralytics.com/images/bus.jpg")[0]

model.export(format="onnx",imgsz=[640,640], opset=12)  # export the model to ONNX format

input(".....................")"""






"""
import openvino as ov

import onnx

onnx_model = onnx.load("yolov8n.onnx")
onnx.checker.check_model(onnx_model)

print("modeled")

core = ov.Core()
print("core")
compiled_model = core.compile_model(onnx_model, "GPU")

print("compiled model")"""










from IPython import display
display.clear_output()
 
import ultralytics
ultralytics.checks()