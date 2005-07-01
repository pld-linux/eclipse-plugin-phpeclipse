Summary:	PHPeclipse - PHP/SQL/HTML Eclipse-Plugin
Summary(pl):	PHPeclipse - wtyczka do Eclipse obs³uguj±ca PHP/SQL/HTML
Name:		eclipse-plugin-phpeclipse
Version:	1.1.4
Release:	2
License:	CPL v1.0
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/phpeclipse/PHPeclipse-%{version}-features.zip
# Source0-md5:	9fd1b3758e815095f44663b752f34838
URL:		http://www.phpeclipse.de
BuildRequires:	unzip
Requires:	eclipse >= 3.1-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_datadir}/eclipse

%description
PHP, SQL, HTML - Support for the Eclipse IDE Framework 
(http://www.eclipse.org/); Some Features are PHP parser, debugger,
code formatter, outline view, templates.

%description -l pl
Wtyczka do obs³ugi PHP, SQL, HTML dla ¶rodowiska Eclipse
(http://www.eclipse.org/); zawiera parser PHP, debugger, formatowanie
kodu, podgl±d szkicu, szablony.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -a eclipse/{plugins,features} $RPM_BUILD_ROOT%{_eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/features/*
%{_eclipsedir}/plugins/*
