%{?_javapackages_macros:%_javapackages_macros}
%global namedtag SP4
%global namedreltag .%{namedtag}
%global namedversion %{version}%{?namedreltag}
%global upstreamversion %{version}-%{namedtag}

Name:             cdi-api1
Version:          1.0
Release:          15%{namedreltag}.1
Summary:          CDI API 1.0
Group:            Development/Java
License:          ASL 2.0
URL:              http://seamframework.org/Weld

# svn export http://anonsvn.jboss.org/repos/weld/cdi-api/tags/1.0-SP4/ cdi-api-1.0.SP4
# tar cafJ cdi-api-1.0.SP4.tar.xz cdi-api-1.0.SP4
Source0:          cdi-api-%{namedversion}.tar.xz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-plugin-build-helper
BuildRequires:    testng
BuildRequires:    jboss-el-2.2-api
BuildRequires:    jboss-interceptors-1.1-api
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    geronimo-annotation
BuildRequires:    geronimo-parent-poms
BuildRequires:    weld-parent
BuildRequires:    jpackage-utils

%description
APIs for JSR-299: Contexts and Dependency Injection for Java EE

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.
Group:            Documentation

%prep
%setup -q -n cdi-api-%{namedversion}

cp %{SOURCE1} .

%build
%mvn_compat_version : %{namedversion} %{upstreamversion} %{version} 1
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Mon Jul 07 2014 Marek Goldmann <mgoldman@redhat.com> - 1.0-15.SP4
- Add compat versions

* Mon Jul 07 2014 Marek Goldmann <mgoldman@redhat.com> - 1.0-14.SP4
- Switch to xmvn

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13.SP4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0-12.SP4
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11.SP4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0-10.SP4
- Created a compat package

* Sat Mar 02 2013 Mat Booth <fedora@matbooth.co.uk> - 1.0-9.SP4
- Add missing BR, fixes FTBFS rhbz #913916

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8.SP4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-7.SP4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Dec 04 2012 Marek Goldmann <mgoldman@redhat.com> - 1.0-6.SP4
- Added missing BR

* Tue Dec 04 2012 Marek Goldmann <mgoldman@redhat.com> - 1.0-5.SP4
- Added missing BR/R
- Simplified the spec file
- Removed unnecessary patch

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4.SP4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 25 2012 Asaf Shakarchi <asaf@redhat.com> 1.0-3.SP4
- Fixed changelog versions.

* Fri Mar 16 2012 Asaf Shakarchi <asaf@redhat.com> 1.0-2.SP4
- Added required dependencies, modified patches and cleaned spec.

* Mon Feb 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.0-1.SP4
- Initial packaging


