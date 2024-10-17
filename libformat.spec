%define	major 2
%define libname	%mklibname format %{major}
%define develname %mklibname -d format

Summary:	A library for HTML syntax highlighting of source code
Name:		libformat
Version:	1.5
Release:	7
Group:		System/Libraries
License:	GPL
URL:		https://daveb.net/format
Source0:	http://daveb.net/format/src/%{name}-%{version}.tar.bz2
Patch0:		libformat-1.5-fix-str-fmt.patch

%description
libformat is an adaptation of the mod_format Apache module to do syntax
highlighting of source code using HTML outside of Apache.  libformat is 
capable of syntax highlighting C, C++, Java, Python, Verilog and VHDL 
source code.  

%package -n	%{libname}
Summary:	A library for HTML syntax highlighting of source code
Group:		System/Libraries

%description -n	%{libname}
libformat is an adaptation of the mod_format Apache module to do syntax
highlighting of source code using HTML outside of Apache.  libformat is 
capable of syntax highlighting C, C++, Java, Python, Verilog and VHDL 
source code.  

%package -n	%{develname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}format2-devel < %{version}-%{release}

%description -n	%{develname}
libformat is an adaptation of the mod_format Apache module to do syntax
highlighting of source code using HTML outside of Apache.  libformat is 
capable of syntax highlighting C, C++, Java, Python, Verilog and VHDL 
source code.  

This package contains the static %{name} library and its header files.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/srcformat
%{_libdir}/*.so.*
%{_datadir}/libformat

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a

%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-5mdv2011.0
+ Revision: 609746
- rebuild

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 1.5-4mdv2010.1
+ Revision: 508565
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.5-3mdv2009.0
+ Revision: 248645
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.5-1mdv2008.1
+ Revision: 140921
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5-1mdv2008.0
+ Revision: 25435
- Import libformat



* Wed Apr 05 2006 Oden Eriksson <oeriksson@mandriva.com> 1.5-1mdk
- initial Mandriva package
