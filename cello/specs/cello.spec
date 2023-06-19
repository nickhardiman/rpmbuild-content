Name:           bello
Version:        0.0.1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/DistTag/
Release:        1%{?dist}
Summary:        A simple hello world script written in Bash
BuildArch:      noarch

License:        GPL
Source0:        %{name}-%{version}.tgz

Requires:       bash

%description
A demo RPM build

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name} $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

%changelog
* Mon Jun 19 2023 Nick <nick@example.com> - 0.0.1
- First version being packaged
