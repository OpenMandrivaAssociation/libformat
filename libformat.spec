%define	major 2
%define libname	%mklibname format %{major}
%define develname %mklibname -d format

Summary:	A library for HTML syntax highlighting of source code
Name:		libformat
Version:	1.5
Release:	%mkrel 4
Group:		System/Libraries
License:	GPL
URL:		http://daveb.net/format
Source0:	http://daveb.net/format/src/%{name}-%{version}.tar.bz2
Patch0:		libformat-1.5-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
libformat is an adaptation of the mod_format Apache module to do syntax
highlighting of source code using HTML outside of Apache.  libformat is 
capable of syntax highlighting C, C++, Java, Python, Verilog and VHDL 
source code.  

%package -n	%{libname}
Summary:	A library for HTML syntax highlighting of source code
Group:          System/Libraries

%description -n	%{libname}
libformat is an adaptation of the mod_format Apache module to do syntax
highlighting of source code using HTML outside of Apache.  libformat is 
capable of syntax highlighting C, C++, Java, Python, Verilog and VHDL 
source code.  

%package -n	%{develname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}
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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/srcformat
%{_libdir}/*.so.*
%{_datadir}/libformat

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
