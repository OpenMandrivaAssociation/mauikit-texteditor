%define major 2

#define snapshot 20220106
%define libname %mklibname MauiKit-texteditor %{major}
%define devname %mklibname -d MauiKit-texteditor

Name:		mauikit-texteditor
Version:	2.2.2
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	MauiKit TextEditor utilities and controls
Url:		http://mauikit.org/
Source0:	https://invent.kde.org/maui/mauikit-texteditor/-/archive/%{?snapshot:master/mauikit-texteditor-master.tar.bz2#/mauikit-texteditor-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/mauikit-texteditor-v%{version}.tar.bz2}

License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	qt5-qtgraphicaleffects
BuildRequires:	qt5-qtdeclarative
BuildRequires:	qt5-qtquickcontrols2

%description
Library for developing MAUI applications

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%package -n %{libname}
Summary:	Library files for mauikit-texteditor
Group:		System/Libraries

%description -n %{libname}
Library files for mauikit-texteditor

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%package -n %{devname}
Summary:	Development files for mauikit-texteditor
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for mauikit-texteditor

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.


%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang mauikittexteditor

%files -n %{libname} -f mauikittexteditor.lang
%{_libdir}/libMauiKitTextEditor.so.%{major}*
%{_libdir}/qt5/qml/org/mauikit/texteditor/

%files -n %{devname}
%{_libdir}/cmake/MauiKitTextEditor/
%{_libdir}/libMauiKitTextEditor.so
%{_includedir}/MauiKit/TextEditor/texteditor_export.h
%{_includedir}/MauiKit/TextEditor/texteditor_version.h
