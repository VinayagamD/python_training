class Utils:

    @staticmethod
    def print_message(message, line="start"):
        print(f"==================== {message} {line} ===========================\n")

    """
        @staticmethod
        def print_message(message, end_line=False):
            print(f"==================== {message} ", "start" if end_line else "start",
             " ===========================\n")
    """

    @staticmethod
    def print_divider():
        print("====================================================================================================\n")
