from httprunner.api import HttpRunner

runner = HttpRunner()
runner.run(r"C:\Users\lzp\Documents\GitHub\api_platform_course\api_platform_httprunner\api\login.yml")
print(runner._summary)
