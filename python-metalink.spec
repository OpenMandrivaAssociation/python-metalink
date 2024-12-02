%define	oname	metalink-library

Summary:	Python library for generating metalinks
Name:		python-metalink
Version:	6.5.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pymetalink/pymetalink-%{version}.tar.gz
URL:		https://github.com/metalink-dev/pymetalink
License:	GPLv2
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	python
BuildSystem:	python

%description
A script based library to create and manage Metalink download files,
which contain HTTP, FTP and P2P download links for single or multiple
download files.

%prep
%autosetup -p1 -n pymetalink-%{version}

%files
%defattr(-,root,root)
%{_bindir}/pymetalink
%{py_puresitedir}/metalink
%{py_puresitedir}/pymetalink-%{version}.dist-info
