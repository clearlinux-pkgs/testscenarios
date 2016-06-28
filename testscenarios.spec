#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : testscenarios
Version  : 0.5.0
Release  : 16
URL      : https://pypi.python.org/packages/source/t/testscenarios/testscenarios-0.5.0.tar.gz
Source0  : https://pypi.python.org/packages/source/t/testscenarios/testscenarios-0.5.0.tar.gz
Summary  : Testscenarios, a pyunit extension for dependency injection
Group    : Development/Tools
License  : Apache-2.0
Requires: testscenarios-python
BuildRequires : extras
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : testtools
BuildRequires : traceback2

%description
*****************************************************************
testscenarios: extensions to python unittest to support scenarios
*****************************************************************

%package python
Summary: python components for the testscenarios package.
Group: Default

%description python
python components for the testscenarios package.


%prep
%setup -q -n testscenarios-0.5.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
py.test-2.7 || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
