select
    disturbance_type.name as disturbance_type_name,
    land_class.is_forest as is_forest
from disturbance_type 
left outer join land_class on
    disturbance_type.transition_land_class_id = land_class.id