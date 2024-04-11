def get_input_output_tensor_names(model):
    # Get the input tensor name
    input_tensor_name = model.input_names[0]  # Assuming there's only one input tensor

    # Get the output tensor name
    output_tensor_name = model.output_names[0]  # Assuming there's only one output tensor

    return input_tensor_name, output_tensor_name

# Load the model
model = self.load_model(self.config.path_of_model)

# Get input and output tensor names
input_tensor_name, output_tensor_name = get_input_output_tensor_names(model)

print("Input Tensor Name:", input_tensor_name)
print("Output Tensor Name:", output_tensor_name)
