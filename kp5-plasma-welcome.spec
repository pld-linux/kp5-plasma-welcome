#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.2
%define		qtver		5.15.2
%define		kpname		plasma-welcome
%define		kf5ver		5.102.0

Summary:	Plasma Welcome App
Name:		kp5-%{kpname}
Version:	5.27.2
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	7a644d7b19055a994feb96fa0b977857
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	ka5-kaccounts-integration-devel
BuildRequires:	kf5-attica-devel >= 5.103.0
BuildRequires:	kf5-extra-cmake-modules >= 5.82
BuildRequires:	kf5-kauth-devel >= 5.103.0
BuildRequires:	kf5-kcodecs-devel >= 5.103.0
BuildRequires:	kf5-kcompletion-devel >= 5.103.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.103.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.97.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.98
BuildRequires:	kf5-kdeclarative-devel >= 5.98
BuildRequires:	kf5-ki18n-devel >= 5.98
BuildRequires:	kf5-kio-devel >= 5.98
BuildRequires:	kf5-kirigami2-devel >= 5.98
BuildRequires:	kf5-kitemviews-devel >= 5.103.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.103.0
BuildRequires:	kf5-knewstuff-devel >= 5.98
BuildRequires:	kf5-knotifications-devel >= 5.98
BuildRequires:	kf5-kpackage-devel >= 5.103.0
BuildRequires:	kf5-kservice-devel >= 5.98
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.103.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.98
BuildRequires:	kf5-kxmlgui-devel >= 5.103.0
BuildRequires:	kf5-plasma-framework-devel >= 5.98
BuildRequires:	kf5-solid-devel >= 5.103.0
BuildRequires:	kuserfeedback-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
A Friendly onboarding wizard for Plasma

Welcome Center is the perfect introduction to KDE Plasma! It can help
you learn how to connect to the internet, install apps, customize the
system, and more!

There are two usage modes:
- Run the app normally and it will show a welcome/onboarding wizard.
- Run the app with the `--after-upgrade-to` argument to show a
  post-upgrade message. For example: `plasma-welcome --after-upgrade-to
  5.25`.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
/etc/xdg/autostart/org.kde.plasma-welcome.desktop
%attr(755,root,root) %{_bindir}/plasma-welcome
%dir %{_libdir}/qt5/qml/org/kde/plasma/welcome
%{_libdir}/qt5/qml/org/kde/plasma/welcome/GenericPage.qml
%{_libdir}/qt5/qml/org/kde/plasma/welcome/KCM.qml
%{_libdir}/qt5/qml/org/kde/plasma/welcome/qmldir
%{_desktopdir}/org.kde.plasma-welcome.desktop
%{_datadir}/metainfo/org.kde.plasma-welcome.appdata.xml
