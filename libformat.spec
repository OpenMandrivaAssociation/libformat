%define	major 2
%define libname	%mklibname format %{major}

Summary:	A library for HTML syntax highlighting of source code
Name:		libformat
Version:	1.5
Release:	%mkrel 4
Group:		System/Libraries
License:	GPL
URL:		http://daveb.net/format
Source0:	http://daveb.net/format/src/%{name}-%{version}.tar.bz2
BuildRequires:	automake1.7
BuildRequires:	autoconf2.5
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

%package -n	%{libname}-devel
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
libformat is an adaptation of the mod_format Apache module to do syntax
highlighting of source code using HTML outside of Apache.  libformat is 
capable of syntax highlighting C, C++, Java, Python, Verilog and VHDL 
source code.  

This package contains the static %{name} library and its header files.

%prep

%setup -q

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal-1.7; automake-1.7 --add-missing --copy; autoconf --force

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

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
