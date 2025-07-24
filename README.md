# 🏥 Hospital Management System

This is a Spring Boot + JPA + MySQL based project that helps manage hospital data like doctors, patients, departments, and insurance.

---

## 💡 Key Features

- Doctor, Patient, Department, Insurance Management
- Blood Group Reporting with DTOs
- Spring Boot + JPA + MySQL Integration
- Clean Layered Architecture
- Real-time Data Reporting using JPQL

---

## 🧱 Technologies Used

- Java
- Spring Boot
- Spring Data JPA
- MySQL
- Maven
- Lombok

---

## 📁 Project Modules

- `Doctor` Entity & CRUD
- `Patient` Entity with `Insurance` & `BloodGroup`
- `Department` Entity with One-to-Many Relationship
- `DTO` Reporting Layer
- Enum: `BloodGroupType`
- Repository Layer (Spring Data JPA)
- Service Layer
- Controller Layer

---

## 🔗 JPA Relationships

- `@OneToOne` → Patient ↔ Insurance
- `@ManyToOne` → Patient → Department
- `@OneToMany` → Department → Patients

---

## 📊 Example Report

### 🔹 Blood Group Count Report

```java
@Query("SELECT new com.nt.dto.BloodGroupCountResponseEntity(p.bloodGroup, COUNT(p)) FROM Patient p GROUP BY p.bloodGroup")
List<BloodGroupCountResponseEntity> countEachBloodGroupType();
