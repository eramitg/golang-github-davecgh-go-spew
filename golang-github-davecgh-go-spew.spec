#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-davecgh-go-spew
Version  : 5215b55f46b2b919f50a1df0eaa5886afe4e3b3d
Release  : 2
URL      : https://github.com/davecgh/go-spew/archive/5215b55f46b2b919f50a1df0eaa5886afe4e3b3d.tar.gz
Source0  : https://github.com/davecgh/go-spew/archive/5215b55f46b2b919f50a1df0eaa5886afe4e3b3d.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : ISC
BuildRequires : go

%description
go-spew
=======
[![Build Status](https://travis-ci.org/davecgh/go-spew.png?branch=master)]
(https://travis-ci.org/davecgh/go-spew) [![Coverage Status]
(https://coveralls.io/repos/davecgh/go-spew/badge.png?branch=master)]
(https://coveralls.io/r/davecgh/go-spew?branch=master)

%prep
%setup -q -n go-spew-5215b55f46b2b919f50a1df0eaa5886afe4e3b3d

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/davecgh/go-spew"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x github.com/davecgh/go-spew/spew

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/bypass.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/bypasssafe.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/common.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/common_test.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/config.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/doc.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/dump.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/dump_test.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/dumpcgo_test.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/dumpnocgo_test.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/example_test.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/format.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/format_test.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/internal_test.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/internalunsafe_test.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/spew.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/spew_test.go
/usr/lib/golang/src/github.com/davecgh/go-spew/spew/testdata/dumpcgo.go
