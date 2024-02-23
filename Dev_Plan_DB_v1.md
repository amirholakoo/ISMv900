![GPT](https://files.oaiusercontent.com/file-ZVg9huG14ovwzZYiwNCDbzzB?se=2124-01-27T06%3A40%3A53Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D1209600%2C%20immutable&rscd=attachment%3B%20filename%3Dcc4cbde8-0ff7-4db8-a442-9e4f793e5755.png&sig=JSkBFTpEQ/ATP86jPYsKov2HLtzS1uiDfrqVwYTemCo%3D)

Dev Mentor

### Database Design Breakdown

1.  Entities and Relationships Identification

    -   Subtasks:
        1.  Analyze the system requirements to list all entities (Shipments, Trucks, Suppliers, Customers, Materials, etc.).
        2.  Define attributes for each entity, considering data types and constraints.
        3.  Identify relationships between entities, including one-to-one, one-to-many, and many-to-many.
        4.  Establish foreign keys and join tables (for many-to-many relationships).
        5.  Create an Entity-Relationship Diagram (ERD) to visualize entities and their relationships.
2.  Django Models Creation

    -   Subtasks:
        1.  Convert each entity into a Django model, defining fields according to identified attributes.
        2.  Use Django ORM relationships (`ForeignKey`, `ManyToManyField`, `OneToOneField`) to implement identified relationships.
        3.  Implement model methods for common operations (e.g., custom save methods, helper functions).
        4.  Define model validators for data integrity and constraints enforcement.
        5.  Use Django migrations to create and update the database schema.
3.  Normalization and Optimization

    -   Subtasks:
        1.  Apply normalization rules (up to 3NF or beyond) to eliminate redundancy and ensure data integrity.
        2.  Analyze queries for common operations to optimize model indexes and database structure.
        3.  Implement soft delete functionality to preserve data by adding an `is_active` or `deleted_at` field instead of physical deletion.
        4.  Consider partitioning large tables or using database views for complex queries.
        5.  Conduct performance testing and adjust the schema based on findings.
4.  Security and Access Control

    -   Subtasks:
        1.  Design models to include user and role management for access control.
        2.  Implement row-level security in PostgreSQL for sensitive data access control.
        3.  Encrypt sensitive fields in the database (e.g., personal information) using Django or PostgreSQL functionalities.
        4.  Use Django's built-in mechanisms for password hashing and session management.
        5.  Regularly update Django and PostgreSQL to their latest secure versions to mitigate vulnerabilities.
5.  Backup, Recovery, and Maintenance

    -   Subtasks:
        1.  Establish a backup strategy, considering full and incremental backups.
        2.  Implement automated scripts for regular database backups.
        3.  Test recovery procedures to ensure data can be restored from backups.
        4.  Plan for database maintenance operations, such as vacuuming in PostgreSQL, to optimize performance.
        5.  Monitor database health and performance, adjusting resources and configurations as necessary.
