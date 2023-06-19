Name:           hello-bash
Version:        0.0.1
Release:        1%{?dist}
Summary:        A simple hello world script written in Bash
BuildArch:      noarch

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       bash

%description
A demo RPM build

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name}.sh $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}.sh

%changelog
* Mon Jun 19 2023 Nick <nick@example.com> - 0.0.1
- First version being packaged
