# custom_input_swapper.py
# Place this file in: ComfyUI/custom_nodes/

class AnyType(str):
    """Special helper that allows the node to accept ANY data type."""
    def __ne__(self, __value: object) -> bool:
        return False

any_type = AnyType("*")


class InputSwapper:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input1": (any_type,),
                "input2": (any_type,),
                "swap": ("BOOLEAN", {
                    "default": False,
                    "label_on": "🔄 Swapped",
                    "label_off": "Normal",
                    "tooltip": "Toggle to invert the two inputs (1↔2)"
                }),
            }
        }

    RETURN_TYPES = (any_type, any_type)
    RETURN_NAMES = ("output1", "output2")
    FUNCTION = "execute"
    CATEGORY = "utils"          # You can change this to any category you like

    def execute(self, input1, input2, swap=False):
        if swap:
            return (input2, input1)   # swapped
        return (input1, input2)       # normal passthrough


# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "InputSwapper": InputSwapper
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "InputSwapper": "🔄 Input Swapper (2→2)"
}