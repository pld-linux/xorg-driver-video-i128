Summary:	X.org video driver for Number 9 I128 video adapters
Summary(pl):	Sterownik obrazu X.org dla kart graficznych Number 9 I128
Name:		xorg-driver-video-i128
Version:	1.1.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-i128-%{version}.tar.bz2
# Source0-md5:	0dd457bb4f1ddf4834e8a643838e985c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Number 9 I128 video adapters. It supports PCI
and AGP video cards based on the following I128 chips: I128 rev 1,
I128-II, I128-T2R (Ticket 2 Ride), I128-T2R4 (Ticket 2 Ride IV).

%description -l pl
Sterownik obrazu X.org dla kart graficznych Number 9 I128. Obs³uguje
karty PCI i AGP oparte na nastêpuj±cych uk³adach I128: I128 rev 1,
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
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/i128_drv.so
%{_mandir}/man4/i128.4x*
