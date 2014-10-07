%define major 5
%define libname %mklibname KF5NotifyConfig %{major}
%define devname %mklibname KF5NotifyConfig -d
%define debug_package %{nil}

Name: knotifyconfig
Version: 5.3.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: Configuration system for knotify
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(Phonon4Qt5)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Notifications)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
Configuration system for knotify

%package -n %{libname}
Summary: The KDE Frameworks 5 NotifyConfig library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
The KDE Frameworks 5 NotifyConfig library

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 NotifyConfig library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 NotifyConfig library

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang knotifyconfig5

%files -f knotifyconfig5.lang

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_prefix}/mkspecs/*
