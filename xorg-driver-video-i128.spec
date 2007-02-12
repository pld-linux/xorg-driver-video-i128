Summary:	X.org video driver for Number 9 I128 video adapters
Summary(pl.UTF-8):   Sterownik obrazu X.org dla kart graficznych Number 9 I128
Name:		xorg-driver-video-i128
Version:	1.2.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-i128-%{version}.tar.bz2
# Source0-md5:	d0080732eaa15059b0a953aa3522185a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Number 9 I128 video adapters. It supports PCI
and AGP video cards based on the following I128 chips: I128 rev 1,
I128-II, I128-T2R (Ticket 2 Ride), I128-T2R4 (Ticket 2 Ride IV).

%description -l pl.UTF-8
Sterownik obrazu X.org dla kart graficznych Number 9 I128. Obsługuje
karty PCI i AGP oparte na następujących układach I128: I128 rev 1,
I128-II, I128-T2R (Ticket 2 Ride), I128-T2R4 (Ticket 2 Ride IV).

%prep
%setup -q -n xf86-video-i128-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/i128_drv.so
%{_mandir}/man4/i128.4*