%define	oname	metalink-library

Summary:	Python library for generating metalinks
Name:		python-metalink
Version:	1.0
Release:	9
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



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.0-8mdv2010.0
+ Revision: 433749
- rebuild
- rebuild

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - rebuild so that module ends up in correct location

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2009.0
+ Revision: 259704
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2009.0
+ Revision: 247511
- rebuild

* Fri Feb 01 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0-2mdv2008.1
+ Revision: 160962
- rebuild since rpm 4.4.2.2 hosed python macros last time..

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 28 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0-1mdv2008.1
+ Revision: 113595
- import python-metalink


* Wed Nov 28 2007 Per �yvind Karlsen <pkarlsen@mandriva.com> 1.0-1mdv2008.1
- Initial release
