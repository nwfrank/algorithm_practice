class Tester:
    def __init__(self):
        self.total_tests = 0
        self.passed_tests = 0

    def _run_test(self, message, func, expected_results, multiple):
        self.total_tests += 1
        error = False
        try:
            actual_result = func()
        except Exception as e:
            actual_result = "\033[31mERROR\033[0m" + ' ' + str(e)
            error = True

        if multiple:
            passed = actual_result in expected_results and not error
            expected_msg = f"Expected to be in: {expected_results}"
        else:
            passed = actual_result == expected_results and not error
            expected_msg = f"Expected: {expected_results}"

        status = "\033[32mTEST PASSED\033[0m" if passed else "\033[31mTEST FAILED\033[0m"
        print(f"{status} -> {message}")
        
        if not passed:
            print(f"{expected_msg}, but got: {actual_result}")
        else:
            self.passed_tests += 1

    def test(self, message, func, expected_result):
        self._run_test(message, func, expected_result, False)

    def test_multiple_possibilities(self, message, func, possible_results):
        self._run_test(message, func, possible_results, True)

    def print_pass_percentage(self):
        if self.total_tests == 0:
            print("\033[33mNo tests ran.\033[0m")
        else:
            pass_percentage = (self.passed_tests / self.total_tests) * 100
            color = "\033[32m" if pass_percentage == 100 else "\033[31m"
            print(f"{color}Tests Passed: {self.passed_tests}/{self.total_tests} ({pass_percentage:.2f}%)\033[0m")
