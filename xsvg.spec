Summary:	X11 SVG viewer
Summary(pl):	Przegl±darka SVG dla X11
Name:		xsvg
Version:	0.1.0
Release:	1
License:	BSD-like
Group:		X11/Applications/Graphics
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	4a08e4b5368052ad0ec5ee2a8be286ed
URL:		http://www.xsvg.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxsvg-devel >= 0.1.0
BuildRequires:	pkgconfig
Requires:	libxsvg >= 0.1.0
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
