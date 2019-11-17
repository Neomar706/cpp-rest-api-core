from conans import ConanFile, tools

class RESTAPICoreConan(ConanFile):
    name = "RESTAPICore"
    description = "C++ REST API framework"
    url = "https://github.com/systelab/cpp-rest-api-core"
    homepage = "https://github.com/systelab/cpp-rest-api-core"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "rest", "api", "framework")
    license = "MIT"
    generators = "cmake_find_package"
    settings = "os", "compiler", "build_type", "arch"
    options = {"gtest": ["1.7.0", "1.8.1"], "OpenSSL": ["1.0.2n"]}
    default_options = {"gtest":"1.8.1", "OpenSSL":"1.0.2n"}

    def configure(self):
        self.options["WebServerAdapterTestUtilities"].gtest = self.options.gtest
        self.options["JSONAdapterTestUtilities"].gtest = self.options.gtest
        self.options["JWTUtils"].gtest = self.options.gtest
        self.options["JWTUtils"].OpenSSL = self.options.OpenSSL

    def build_requirements(self):
        self.build_requires("TestUtilitiesInterface/1.0.3@systelab/stable")
        self.build_requires("WebServerAdapterTestUtilities/1.0.2@systelab/stable")
        self.build_requires("JSONAdapterTestUtilities/1.0.4@systelab/stable")
        if self.options.gtest == "1.7.0":
            self.build_requires("gtest/1.7.0@systelab/stable")
        else:
            self.build_requires("gtest/1.8.1@bincrafters/stable")

    def requirements(self):
        self.requires("WebServerAdapterInterface/1.0.2@systelab/stable")
        self.requires("JWTUtils/1.0.4@systelab/stable")

    def imports(self):
        self.copy("*.dll", dst=("bin/%s" % self.settings.build_type), src="bin")
        self.copy("*.dylib*", dst=("bin/%s" % self.settings.build_type), src="lib")
        self.copy("*.so*", dst=("bin/%s" % self.settings.build_type), src="lib")

    def package(self):
        self.copy("*.h", dst="include/RESTAPICore", src="src/RESTAPICore")
        self.copy("*RESTAPICore.lib", dst="lib", keep_path=False)
        self.copy("*RESTAPICore.pdb", dst="lib", keep_path=False)
        self.copy("*RESTAPICore.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
