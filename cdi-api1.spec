%{?_javapackages_macros:%_javapackages_macros}
%global namedtag SP4
%global namedreltag .%{namedtag}
%global namedversion %{version}%{?namedreltag}
%global upstreamversion %{version}-%{namedtag}

Name:             cdi-api1
Version:          1.0
Release:          11%{namedreltag}.0%{?dist}
Summary:          CDI API 1.0

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

Requires:         jpackage-utils
Requires:         java
Requires:         jboss-el-2.2-api
Requires:         jboss-interceptors-1.1-api
Requires:         jboss-ejb-3.1-api
Requires:         geronimo-annotation

%description
APIs for JSR-299: Contexts and Dependency Injection for Java EE

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

Requires:         jpackage-utils

%prep
%setup -q -n cdi-api-%{namedversion}

cp %{SOURCE1} .

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

# JAR
install -pm 644 target/cdi-api-%{upstreamversion}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar

# POM
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom

%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar -v "1,%{upstreamversion}"

# JAVADOC
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE-2.0.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
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

