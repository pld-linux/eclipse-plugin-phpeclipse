Summary:	PHPeclipse - PHP/SQL/HTML Eclipse-Plugin
Summary(pl):	PHPeclipse - Wtyczka do Eclipse obs³uguj±ca PHP/SQL/HTML
Name:		eclipse-plugin-phpeclipse
Version:	1.1.3
%define		thisversionbuilddate	2005-01-29
Release:	1
License:	CPL v1.0
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/sourceforge/phpeclipse/PHPEclipse%{version}-%{thisversionbuilddate}.zip
# Source0-md5:	a73cbf6c0862de5caf90d848b3f58302
URL:		http://www.phpeclipse.de
BuildRequires:	unzip
Requires:	eclipse >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_libdir}/eclipse

%description
PHP, SQL, HTML - Support for the Eclipse IDE Framework 
(www.eclipse.org); Some Features are PHP parser, debugger, 
code formatter, outline view, templates.
%description -l pl

Wtyczka do obs³ugi PHP, SQL, HTML dla ¶rodowiska Eclipse
(www.eclipse.org); Zawiera parser PHP, debugger, formatowanie
kodu, podgl±d szkicu, szablony.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -r plugins features $RPM_BUILD_ROOT%{_eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/features/*
%{_eclipsedir}/plugins/*
