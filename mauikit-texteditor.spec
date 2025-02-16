%define major 4

#define snapshot 20220106
%define libname %mklibname MauiKit-texteditor
%define oldlibname %mklibname MauiKit-texteditor 3
%define devname %mklibname -d MauiKit-texteditor

Name:		mauikit-texteditor
Version:	4.0.1
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	MauiKit TextEditor utilities and controls
Url:		https://mauikit.org/
Source0:	https://invent.kde.org/maui/mauikit-texteditor/-/archive/%{?snapshot:master/mauikit-texteditor-master.tar.bz2#/mauikit-texteditor-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/mauikit-texteditor-v%{version}.tar.bz2}

License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit4)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebEngineCore)


%description
Library for developing MAUI applications

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%package -n %{libname}
Summary:	Library files for mauikit-texteditor
Group:		System/Libraries
%rename %{oldlibname}

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
%{_libdir}/libMauiKitTextEditor4.so.%{major}*
%{_libdir}/qt6/qml/org/mauikit/texteditor/

%files -n %{devname}
%{_libdir}/cmake/MauiKitTextEditor4/
%{_libdir}/libMauiKitTextEditor4.so
%{_includedir}/MauiKit4/TextEditor/texteditor_export.h
%{_includedir}/MauiKit4/TextEditor/texteditor_version.h
%{_includedir}/MauiKit4/TextEditor/moduleinfo.h
