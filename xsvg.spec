Summary:	X11 SVG viewer
Summary(pl):	Przegl±darka SVG dla X11
Name:		xsvg
Version:	0.1.2
Release:	1
License:	BSD-like
Group:		X11/Applications/Graphics
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	4c54ec3e66671465e86f8cfba6220ea4
URL:		http://www.xsvg.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsvg-cairo-devel >= 0.1.3
BuildRequires:	pkgconfig
Requires:	libsvg-cairo >= 0.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xsvg program is a viewer for SVG files.

%description -l pl
Program xsvg to przegl±darka plików SVG.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
