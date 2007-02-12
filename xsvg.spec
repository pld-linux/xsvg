Summary:	X11 SVG viewer
Summary(pl.UTF-8):   Przeglądarka SVG dla X11
Name:		xsvg
Version:	0.2.1
Release:	2
License:	BSD-like
Group:		X11/Applications/Graphics
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	f20409e87d9bff3c4d698d8c0e9e9f2b
URL:		http://www.xsvg.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsvg-cairo-devel >= 0.1.6
BuildRequires:	pkgconfig
Requires:	libsvg-cairo >= 0.1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xsvg program is a viewer for SVG files.

%description -l pl.UTF-8
Program xsvg to przeglądarka plików SVG.

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

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xsvg
%{_mandir}/man1/xsvg.1*
