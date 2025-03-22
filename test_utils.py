class Tester:
    def __init__(self):
        self.total_tests = 0
        self.passed_tests = 0

    def test(self, message, func, expected_result):
        self.total_tests += 1
        try:
            actual_result = func()
        except Exception as e:
            actual_result = "\033[31mERROR\033[0m" + ' ' + str(e)
        status = "\033[32mTEST PASSED\033[0m" if actual_result == expected_result else "\033[31mTEST FAILED\033[0m"
        print(f"{status} -> {message}")
        if actual_result != expected_result:
            print(f"Expected: {expected_result}, but got: {actual_result}")
        else:
            self.passed_tests += 1

    def print_pass_percentage(self):
        if self.total_tests == 0:
            print("\033[33mNo tests ran.\033[0m")
        else:
            pass_percentage = (self.passed_tests / self.total_tests) * 100
            # Set the color based on whether 100% tests passed
            color = "\033[32m" if pass_percentage == 100 else "\033[31m"
            print(f"{color}Tests Passed: {self.passed_tests}/{self.total_tests} ({pass_percentage:.2f}%)\033[0m")
