%define	oname	metalink-library

Summary:	Python library for generating metalinks
Name:		python-metalink
Version:	1.0
Release:	%mkrel 7
Source0:	http://metalink-library.googlecode.com/files/%{oname}-%{version}.tar.bz2
URL:		http://code.google.com/p/metalink-library/
License:	GPLv2
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
A script based library to create and manage Metalink download files,
which contain HTTP, FTP and P2P download links for single or multiple
download files.

%prep
%setup -q -c -n %{oname}-%{version} -a 0

%build

%install
rm -rf %{buildroot}
install -m644 metalink.py -D %{buildroot}%{python_sitelib}/metalink.py

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/metalink.py

